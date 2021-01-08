---
title: Transferable.getTransferData()
permalink: Java/Transferable/getTransferData
date: 2021-01-04
key: JavaJava.T.Transferable
category: java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Transferable.metodos valor="getTransferData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getTransferData(DataFlavor flavor) throws UnsupportedFlavorException, IOException
~~~

## Parámetros
* **DataFlavor flavor**,  {% include w3api/param_description.html metodo=_data parametro="DataFlavor flavor" %}

## Excepciones
[UnsupportedFlavorException](/Java/UnsupportedFlavorException/), [IOException](/Java/IOException/)

## Clase Padre
[Transferable](/Java/Transferable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Transferable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
