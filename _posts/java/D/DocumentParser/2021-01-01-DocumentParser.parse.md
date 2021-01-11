---
title: DocumentParser.parse()
permalink: Java/DocumentParser/parse
date: 2021-01-11
key: JavaJava.D.DocumentParser
category: java
tags: ['java se', 'javax.swing.text.html.parser', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentParser.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void parse(Reader in, HTMLEditorKit.ParserCallback callback, boolean ignoreCharSet) throws IOException
~~~

## Parámetros
* **HTMLEditorKit.ParserCallback callback**,  {% include w3api/param_description.html metodo=_dato parametro="HTMLEditorKit.ParserCallback callback" %}
* **boolean ignoreCharSet**,  {% include w3api/param_description.html metodo=_dato parametro="boolean ignoreCharSet" %}
* **Reader in**,  {% include w3api/param_description.html metodo=_dato parametro="Reader in" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[DocumentParser](/Java/DocumentParser/)

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
