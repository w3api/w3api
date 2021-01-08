---
title: DataContentHandler.getTransferData()
permalink: Java/DataContentHandler/getTransferData
date: 2021-01-04
key: JavaJava.D.DataContentHandler
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataContentHandler.metodos valor="getTransferData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getTransferData(DataFlavor df, DataSource ds) throws UnsupportedFlavorException, IOException
~~~

## Parámetros
* **DataFlavor df**,  {% include w3api/param_description.html metodo=_data parametro="DataFlavor df" %}
* **DataSource ds**,  {% include w3api/param_description.html metodo=_data parametro="DataSource ds" %}

## Excepciones
[UnsupportedFlavorException](/Java/UnsupportedFlavorException/), [IOException](/Java/IOException/)

## Clase Padre
[DataContentHandler](/Java/DataContentHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataContentHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
