---
title: DiagnosticCollector.getDiagnostics()
permalink: Java/DiagnosticCollector/getDiagnostics
date: 2021-01-11
key: JavaJava.D.DiagnosticCollector
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DiagnosticCollector.metodos valor="getDiagnostics" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public List<Diagnostic<? extends S>> getDiagnostics()
~~~

## Clase Padre
[DiagnosticCollector](/Java/DiagnosticCollector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
