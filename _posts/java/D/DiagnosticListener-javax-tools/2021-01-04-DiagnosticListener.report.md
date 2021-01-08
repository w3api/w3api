---
title: DiagnosticListener.report()
permalink: Java/DiagnosticListener-javax-tools/report
date: 2021-01-04
key: JavaJava.D.DiagnosticListener-javax-tools
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DiagnosticListener-javax-tools.metodos valor="report" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void report(Diagnostic<? extends S> diagnostic)
~~~

## Parámetros
* **Diagnostic&lt;? extends S&gt; diagnostic**,  {% include w3api/param_description.html metodo=_data parametro="Diagnostic<? extends S> diagnostic" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DiagnosticListener](/Java/DiagnosticListener-javax-tools/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DiagnosticListener-javax-tools.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
