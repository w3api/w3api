---
title: CardPermission.implies()
permalink: /Java/CardPermission/implies/
date: 2021-01-11
key: Java.C.CardPermission
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardPermission.metodos valor="implies" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean implies(Permission permission)
~~~

## Parámetros
* **Permission permission**,  {% include w3api/param_description.html metodo=_dato parametro="Permission permission" %}

## Clase Padre
[CardPermission](/Java/CardPermission/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
