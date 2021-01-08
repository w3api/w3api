---
title: DataFlavor.getReaderForText()
permalink: Java/DataFlavor/getReaderForText
date: 2021-01-04
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
* **Transferable transferable**,  {% include w3api/param_description.html metodo=_data parametro="Transferable transferable" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedFlavorException](/Java/UnsupportedFlavorException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[DataFlavor](/Java/DataFlavor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataFlavor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
