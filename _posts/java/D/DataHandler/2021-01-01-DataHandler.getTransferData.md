---
title: DataHandler.getTransferData()
permalink: Java/DataHandler/getTransferData
date: 2021-01-11
key: JavaJava.D.DataHandler
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataHandler.metodos valor="getTransferData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getTransferData(DataFlavor flavor) throws UnsupportedFlavorException, IOException
~~~

## Parámetros
* **DataFlavor flavor**,  {% include w3api/param_description.html metodo=_dato parametro="DataFlavor flavor" %}

## Excepciones
[UnsupportedFlavorException](/Java/UnsupportedFlavorException/), [IOException](/Java/IOException/)

## Clase Padre
[DataHandler](/Java/DataHandler/)

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
