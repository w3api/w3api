---
title: EditorKit.write()
permalink: Java/EditorKit/write
date: 2021-01-04
key: JavaJava.E.EditorKit
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EditorKit.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void write(OutputStream out, Document doc, int pos, int len) throws IOException, BadLocationException
public abstract void write(Writer out, Document doc, int pos, int len) throws IOException, BadLocationException
~~~

## Parámetros
* **Writer out**,  {% include w3api/param_description.html metodo=_data parametro="Writer out" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
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
