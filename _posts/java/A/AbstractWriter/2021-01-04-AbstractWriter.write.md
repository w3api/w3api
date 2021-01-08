---
title: AbstractWriter.write()
permalink: Java/AbstractWriter/write
date: 2021-01-04
key: JavaJava.A.AbstractWriter
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractWriter.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract void write() throws IOException, BadLocationException
protected void write(char ch) throws IOException
protected void write(char[] chars, int startIndex, int length) throws IOException
protected void write(String content) throws IOException
~~~

## Parámetros
* **char ch**,  {% include w3api/param_description.html metodo=_data parametro="char ch" %}
* **int startIndex**,  {% include w3api/param_description.html metodo=_data parametro="int startIndex" %}
* **char[] chars**,  {% include w3api/param_description.html metodo=_data parametro="char[] chars" %}
* **String content**,  {% include w3api/param_description.html metodo=_data parametro="String content" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/), [IOException](/Java/IOException/)

## Clase Padre
[AbstractWriter](/Java/AbstractWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
