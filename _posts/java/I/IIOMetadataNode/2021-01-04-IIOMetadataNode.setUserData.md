---
title: IIOMetadataNode.setUserData()
permalink: Java/IIOMetadataNode/setUserData
date: 2021-01-04
key: JavaJava.I.IIOMetadataNode
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadataNode.metodos valor="setUserData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object setUserData(String key, Object data, UserDataHandler handler) throws DOMException
~~~

## Parámetros
* **UserDataHandler handler**,  {% include w3api/param_description.html metodo=_data parametro="UserDataHandler handler" %}
* **Object data**,  {% include w3api/param_description.html metodo=_data parametro="Object data" %}
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[IIOMetadataNode](/Java/IIOMetadataNode/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOMetadataNode.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
