---
title: TabularData.remove()
permalink: /Java/TabularData/remove/
date: 2021-01-11
key: Java.T.TabularData
category: Java
tags: ['java se', 'javax.management.openmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TabularData.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompositeData remove(Object[] key)
~~~

## Parámetros
* **Object[] key**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] key" %}

## Excepciones
[InvalidKeyException](/Java/InvalidKeyException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TabularData](/Java/TabularData/)

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
