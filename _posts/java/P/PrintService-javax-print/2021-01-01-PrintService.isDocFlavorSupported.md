---
title: PrintService.isDocFlavorSupported()
permalink: /Java/PrintService-javax-print/isDocFlavorSupported/
date: 2021-01-11
key: Java.P.PrintService-javax-print
category: Java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintService-javax-print.metodos valor="isDocFlavorSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isDocFlavorSupported(DocFlavor flavor)
~~~

## Parámetros
* **DocFlavor flavor**,  {% include w3api/param_description.html metodo=_dato parametro="DocFlavor flavor" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PrintService](/Java/PrintService-javax-print/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
