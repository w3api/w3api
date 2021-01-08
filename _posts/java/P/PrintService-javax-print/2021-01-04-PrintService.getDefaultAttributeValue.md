---
title: PrintService.getDefaultAttributeValue()
permalink: Java/PrintService-javax-print/getDefaultAttributeValue
date: 2021-01-04
key: JavaJava.P.PrintService-javax-print
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintService-javax-print.metodos valor="getDefaultAttributeValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getDefaultAttributeValue(Class<? extends Attribute> category)
~~~

## Parámetros
* **Class&lt;? extends Attribute&gt; category**,  {% include w3api/param_description.html metodo=_data parametro="Class<? extends Attribute> category" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PrintService](/Java/PrintService-javax-print/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintService-javax-print.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
