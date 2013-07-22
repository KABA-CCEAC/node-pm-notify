#ifndef _PM_H
#define _PM_H

#include <node.h>
#include <v8.h>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "nan.h"

void InitPM();

void Start();

void Stop();

void Notify(char* msg);

#endif