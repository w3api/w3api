---
title: ToolProvider.run()
permalink: /Java/ToolProvider-java-util-spi/run/
date: 2021-01-11
key: Java.T.ToolProvider-java-util-spi
category: Java
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
* **PrintStream err**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream err" %}
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintWriter out" %}
* **PrintWriter err**,  {% include w3api/param_description.html metodo=_dato parametro="PrintWriter err" %}
* **String... args**,  {% include w3api/param_description.html metodo=_dato parametro="String... args" %}
* **PrintStream out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream out" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
