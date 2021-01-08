---
title: ToolProvider.run()
permalink: Java/ToolProvider-java-util-spi/run
date: 2021-01-04
key: JavaJava.T.ToolProvider-java-util-spi
category: java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ToolProvider-java-util-spi.metodos valor="run" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default int run(PrintStream out, PrintStream err, String... args)
int run(PrintWriter out, PrintWriter err, String... args)
~~~

## Parámetros
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_data parametro="PrintWriter out" %}
* **PrintWriter err**,  {% include w3api/param_description.html metodo=_data parametro="PrintWriter err" %}
* **PrintStream out**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream out" %}
* **PrintStream err**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream err" %}
* **String... args**,  {% include w3api/param_description.html metodo=_data parametro="String... args" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ToolProvider](/Java/ToolProvider-java-util-spi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ToolProvider-java-util-spi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
