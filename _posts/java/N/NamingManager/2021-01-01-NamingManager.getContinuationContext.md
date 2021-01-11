---
title: NamingManager.getContinuationContext()
permalink: Java/NamingManager/getContinuationContext
date: 2021-01-11
key: JavaJava.N.NamingManager
category: java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamingManager.metodos valor="getContinuationContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Context getContinuationContext(CannotProceedException cpe) throws NamingException
~~~

## Parámetros
* **CannotProceedException cpe**,  {% include w3api/param_description.html metodo=_dato parametro="CannotProceedException cpe" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[NamingManager](/Java/NamingManager/)

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
