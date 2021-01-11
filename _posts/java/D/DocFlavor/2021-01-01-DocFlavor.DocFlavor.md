---
title: DocFlavor.DocFlavor()
permalink: Java/DocFlavor/DocFlavor
date: 2021-01-11
key: JavaJava.D.DocFlavor
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocFlavor.constructores valor="DocFlavor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DocFlavor(String mimeType, String className)
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DocFlavor](/Java/DocFlavor/)

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
