---
title: ErrorListener.warning()
permalink: /Java/ErrorListener/warning/
date: 2021-01-11
key: Java.E.ErrorListener
category: Java
tags: ['java se', 'javax.xml.transform', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ErrorListener.metodos valor="warning" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void warning(TransformerException exception) throws TransformerException
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
