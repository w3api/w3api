---
title: Clipboard.getData()
permalink: /Java/Clipboard-java-awt-datatransfer/getData/
date: 2021-01-11
key: Java.C.Clipboard-java-awt-datatransfer
category: Java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Clipboard-java-awt-datatransfer.metodos valor="getData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getData(DataFlavor flavor) throws UnsupportedFlavorException, IOException
~~~

## Parámetros
* **DataFlavor flavor**,  {% include w3api/param_description.html metodo=_dato parametro="DataFlavor flavor" %}

## Excepciones
[IOException](/Java/IOException/), [UnsupportedFlavorException](/Java/UnsupportedFlavorException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Clipboard](/Java/Clipboard-java-awt-datatransfer/)

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
