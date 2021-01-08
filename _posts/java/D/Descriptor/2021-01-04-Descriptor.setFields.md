---
title: Descriptor.setFields()
permalink: Java/Descriptor/setFields
date: 2021-01-04
key: JavaJava.D.Descriptor
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.Descriptor.metodos valor="setFields" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setFields(String[] fieldNames, Object[] fieldValues) throws RuntimeOperationsException
~~~

## Parámetros
* **String[] fieldNames**,  {% include w3api/param_description.html metodo=_data parametro="String[] fieldNames" %}
* **Object[] fieldValues**,  {% include w3api/param_description.html metodo=_data parametro="Object[] fieldValues" %}

## Excepciones
[RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[Descriptor](/Java/Descriptor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.Descriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
