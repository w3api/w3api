---
title: TIFFDirectory.createFromMetadata()
permalink: Java/TIFFDirectory/createFromMetadata
date: 2021-01-04
key: JavaJava.T.TIFFDirectory
category: java
tags: ['java se', 'javax.imageio.plugins.tiff', 'java.desktop', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TIFFDirectory.metodos valor="createFromMetadata" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static TIFFDirectory createFromMetadata(IIOMetadata tiffImageMetadata) throws IIOInvalidTreeException
~~~

## Parámetros
* **IIOMetadata tiffImageMetadata**,  {% include w3api/param_description.html metodo=_data parametro="IIOMetadata tiffImageMetadata" %}

## Excepciones
[IIOInvalidTreeException](/Java/IIOInvalidTreeException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TIFFDirectory](/Java/TIFFDirectory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TIFFDirectory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
