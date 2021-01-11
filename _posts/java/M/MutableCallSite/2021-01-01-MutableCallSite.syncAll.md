---
title: MutableCallSite.syncAll()
permalink: Java/MutableCallSite/syncAll
date: 2021-01-11
key: JavaJava.M.MutableCallSite
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MutableCallSite.metodos valor="syncAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void syncAll(MutableCallSite[] sites)
~~~

## Parámetros
* **MutableCallSite[] sites**,  {% include w3api/param_description.html metodo=_dato parametro="MutableCallSite[] sites" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MutableCallSite](/Java/MutableCallSite/)

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
