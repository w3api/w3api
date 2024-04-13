---
title: AbstractWriter.output()
permalink: /Java/AbstractWriter/output/
date: 2021-01-11
key: Java.A.AbstractWriter
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractWriter.metodos valor="output" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void output(char[] content, int start, int length) throws IOException
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **char[] content**,  {% include w3api/param_description.html metodo=_dato parametro="char[] content" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[AbstractWriter](/Java/AbstractWriter/)

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
