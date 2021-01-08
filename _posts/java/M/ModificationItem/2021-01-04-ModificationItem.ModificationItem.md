---
title: ModificationItem.ModificationItem()
permalink: Java/ModificationItem/ModificationItem
date: 2021-01-04
key: JavaJava.M.ModificationItem
category: java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModificationItem.constructores valor="ModificationItem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModificationItem(int mod_op, Attribute attr)
~~~

## Parámetros
* **int mod_op**,  {% include w3api/param_description.html metodo=_data parametro="int mod_op" %}
* **Attribute attr**,  {% include w3api/param_description.html metodo=_data parametro="Attribute attr" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ModificationItem](/Java/ModificationItem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.ModificationItem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
