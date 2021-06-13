---
title: CardPermission.CardPermission()
permalink: /Java/CardPermission/CardPermission/
date: 2021-01-11
key: Java.C.CardPermission
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardPermission.constructores valor="CardPermission" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CardPermission(String terminalName, String actions)
~~~

## Parámetros
* **String actions**,  {% include w3api/param_description.html metodo=_dato parametro="String actions" %}
* **String terminalName**,  {% include w3api/param_description.html metodo=_dato parametro="String terminalName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CardPermission](/Java/CardPermission/)

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
