def main():
    """Run the main script."""
    parser, inspect_parser, query_parser = make_parser()
    args = parser.parse_args()

    # Extract data from the data files into structured Python objects.
    database = NEODatabase(load_neos(args.neofile), load_approaches(args.cadfile))

    # Run the chosen subcommand.
    if args.cmd == 'inspect':
        inspect(database, pdes=args.pdes, name=args.name, verbose=args.verbose)
    elif args.cmd == 'query':
        query(database, args)
    elif args.cmd == 'interactive':
        NEOShell(database, inspect_parser, query_parser, aggressive=args.aggressive).cmdloop()


if __name__ == '__main__':
    main()