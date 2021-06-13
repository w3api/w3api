---
title: StringSelection.getTransferData()
permalink: /Java/StringSelection/getTransferData/
date: 2021-01-11
key: Java.S.StringSelection
category: Java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringSelection.metodos valor="getTransferData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getTransferData(DataFlavor flavor) throws UnsupportedFlavorException, IOException
~~~

## Parámetros
* **DataFlavor flavor**,  {% include w3api/param_description.html metodo=_dato parametro="DataFlavor flavor" %}

## Excepciones
[UnsupportedFlavorException](/Java/UnsupportedFlavorException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[StringSelection](/Java/StringSelection/)

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
