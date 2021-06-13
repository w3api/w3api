---
title: PrintService.isAttributeCategorySupported()
permalink: /Java/PrintService-javax-print/isAttributeCategorySupported/
date: 2021-01-11
key: Java.P.PrintService-javax-print
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintService-javax-print.metodos valor="isAttributeCategorySupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isAttributeCategorySupported(Class<? extends Attribute> category)
~~~

## Parámetros
* **Class&lt;? extends Attribute&gt; category**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Attribute> category" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrintService](/Java/PrintService-javax-print/)

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
