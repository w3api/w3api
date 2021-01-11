---
title: DocFlavor.getParameter()
permalink: Java/DocFlavor/getParameter
date: 2021-01-11
key: JavaJava.D.DocFlavor
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocFlavor.metodos valor="getParameter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getParameter(String paramName)
~~~

## Parámetros
* **String paramName**,  {% include w3api/param_description.html metodo=_dato parametro="String paramName" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
