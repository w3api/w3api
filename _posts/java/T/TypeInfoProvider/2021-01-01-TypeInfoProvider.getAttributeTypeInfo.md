---
title: TypeInfoProvider.getAttributeTypeInfo()
permalink: /Java/TypeInfoProvider/getAttributeTypeInfo/
date: 2021-01-11
key: Java.T.TypeInfoProvider
category: Java
tags: ['java se', 'javax.xml.validation', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TypeInfoProvider.metodos valor="getAttributeTypeInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract TypeInfo getAttributeTypeInfo(int index)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[TypeInfoProvider](/Java/TypeInfoProvider/)

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
