---
title: RequiredModelMBean.getAttributes()
permalink: /Java/RequiredModelMBean/getAttributes/
date: 2021-01-11
key: Java.R.RequiredModelMBean
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RequiredModelMBean.metodos valor="getAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public AttributeList getAttributes(String[] attrNames)
~~~

## Parámetros
* **String[] attrNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] attrNames" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[RequiredModelMBean](/Java/RequiredModelMBean/)

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
