---
title: CharacterData.deleteData()
permalink: /Java/CharacterData/deleteData/
date: 2021-01-11
key: Java.C.CharacterData
category: Java
tags: ['java se', 'org.w3c.dom', 'java.xml', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CharacterData.metodos valor="deleteData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void deleteData(int offset, int count) throws DOMException
~~~

## Parámetros
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[CharacterData](/Java/CharacterData/)

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
