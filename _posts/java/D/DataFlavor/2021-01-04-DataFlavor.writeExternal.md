---
title: DataFlavor.writeExternal()
permalink: Java/DataFlavor/writeExternal
date: 2021-01-04
key: JavaJava.D.DataFlavor
category: java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataFlavor.metodos valor="writeExternal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeExternal(ObjectOutput os) throws IOException
~~~

## Parámetros
* **ObjectOutput os**,  {% include w3api/param_description.html metodo=_data parametro="ObjectOutput os" %}

## Excepciones
[IOException](/Java/IOException/)

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
