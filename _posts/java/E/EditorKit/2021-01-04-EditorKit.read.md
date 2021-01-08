---
title: EditorKit.read()
permalink: Java/EditorKit/read
date: 2021-01-04
key: JavaJava.E.EditorKit
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EditorKit.metodos valor="read" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void read(InputStream in, Document doc, int pos) throws IOException, BadLocationException
public abstract void read(Reader in, Document doc, int pos) throws IOException, BadLocationException
~~~

## Parámetros
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **Reader in**,  {% include w3api/param_description.html metodo=_data parametro="Reader in" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}
* **Document doc**,  {% include w3api/param_description.html metodo=_data parametro="Document doc" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IOException](/Java/IOException/)

## Clase Padre
[EditorKit](/Java/EditorKit/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EditorKit.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
