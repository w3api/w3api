---
title: IIOMetadata.setFromTree()
permalink: /Java/IIOMetadata/setFromTree/
date: 2021-01-11
key: Java.I.IIOMetadata
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadata.metodos valor="setFromTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFromTree(String formatName, Node root) throws IIOInvalidTreeException
~~~

## Parámetros
* **Node root**,  {% include w3api/param_description.html metodo=_dato parametro="Node root" %}
* **String formatName**,  {% include w3api/param_description.html metodo=_dato parametro="String formatName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IIOInvalidTreeException](/Java/IIOInvalidTreeException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[IIOMetadata](/Java/IIOMetadata/)

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
