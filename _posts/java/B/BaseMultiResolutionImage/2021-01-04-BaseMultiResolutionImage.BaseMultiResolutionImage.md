---
title: BaseMultiResolutionImage.BaseMultiResolutionImage()
permalink: Java/BaseMultiResolutionImage/BaseMultiResolutionImage
date: 2021-01-04
key: JavaJava.B.BaseMultiResolutionImage
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseMultiResolutionImage.constructores valor="BaseMultiResolutionImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BaseMultiResolutionImage(int baseImageIndex, Image... resolutionVariants)
public BaseMultiResolutionImage(Image... resolutionVariants)
~~~

## Parámetros
* **Image... resolutionVariants**,  {% include w3api/param_description.html metodo=_data parametro="Image... resolutionVariants" %}
* **int baseImageIndex**,  {% include w3api/param_description.html metodo=_data parametro="int baseImageIndex" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BaseMultiResolutionImage](/Java/BaseMultiResolutionImage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BaseMultiResolutionImage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
