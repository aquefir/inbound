/**********************************************************************\
 *           Inbound, an agnostic software building system.           *
 *                                                                    *
 *             Written by  Alexander Nicholi <//nich.fi/>             *
 *   Copyright (C) 2024-2025 Aquefir Consulting LLC <//aquefir.co/>   *
 *                    Released under BSD-2-Clause.                    *
\**********************************************************************/

#include <stdio.h>

static const char * const s = "_BB_CSZ=%lu _BB_SSZ=%lu _BB_ISZ=%lu _BB_"
"LSZ=%lu _BB_PSZ=%lu _BB_FSZ=%lu _BB_DSZ=%lu _BB_LDSZ=%lu \n";

int main( int ac, char * av[] )
{
	/* discard unused parameters */
	(void)ac;
	(void)av;

	printf( s,
		sizeof(char),
		sizeof(short),
		sizeof(int),
		sizeof(long),
		sizeof(void *),
		sizeof(float),
		sizeof(double),
		sizeof(long double)
	);

	return 0;
}
