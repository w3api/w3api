---
title: ErrorListener.error()
permalink: Java/ErrorListener/error
date: 2021-01-11
key: JavaJava.E.ErrorListener
category: java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ErrorListener.metodos valor="error" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void error(TransformerException exception) throws TransformerException
~~~

## Parámetros
* **TransformerException exception**,  {% include w3api/param_description.html metodo=_dato parametro="TransformerException exception" %}

## Excepciones
[TransformerException](/Java/TransformerException/)

## Clase Padre
[ErrorListener](/Java/ErrorListener/)

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
