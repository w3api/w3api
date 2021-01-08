---
title: ObjectName.apply()
permalink: Java/ObjectName/apply
date: 2021-01-04
key: JavaJava.O.ObjectName
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectName.metodos valor="apply" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean apply(ObjectName name)
~~~

## Parámetros
* **ObjectName name**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName name" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ObjectName](/Java/ObjectName/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectName.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
