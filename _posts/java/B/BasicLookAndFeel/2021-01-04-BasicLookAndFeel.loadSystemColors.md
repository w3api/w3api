---
title: BasicLookAndFeel.loadSystemColors()
permalink: Java/BasicLookAndFeel/loadSystemColors
date: 2021-01-04
key: JavaJava.B.BasicLookAndFeel
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicLookAndFeel.metodos valor="loadSystemColors" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void loadSystemColors(UIDefaults table, String[] systemColors, boolean useNative)
~~~

## Parámetros
* **boolean useNative**,  {% include w3api/param_description.html metodo=_data parametro="boolean useNative" %}
* **String[] systemColors**,  {% include w3api/param_description.html metodo=_data parametro="String[] systemColors" %}
* **UIDefaults table**,  {% include w3api/param_description.html metodo=_data parametro="UIDefaults table" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BasicLookAndFeel](/Java/BasicLookAndFeel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicLookAndFeel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
