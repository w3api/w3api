---
title: DataFlavor.getReaderForText()
permalink: Java/DataFlavor/getReaderForText
date: 2021-01-11
key: JavaJava.D.DataFlavor
category: java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataFlavor.metodos valor="getReaderForText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Reader getReaderForText(Transferable transferable) throws UnsupportedFlavorException, IOException
~~~

## Parámetros
* **Transferable transferable**,  {% include w3api/param_description.html metodo=_dato parametro="Transferable transferable" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [UnsupportedFlavorException](/Java/UnsupportedFlavorException/), [UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DataFlavor](/Java/DataFlavor/)

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
