---
title: Descriptor.getFieldValues()
permalink: /Java/Descriptor/getFieldValues/
date: 2021-01-11
key: Java.D.Descriptor
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.Descriptor.metodos valor="getFieldValues" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object[] getFieldValues(String... fieldNames)
~~~

## Parámetros
* **String... fieldNames**,  {% include w3api/param_description.html metodo=_dato parametro="String... fieldNames" %}

## Clase Padre
[Descriptor](/Java/Descriptor/)

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
