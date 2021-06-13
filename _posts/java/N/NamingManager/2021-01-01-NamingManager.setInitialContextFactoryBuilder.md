---
title: NamingManager.setInitialContextFactoryBuilder()
permalink: /Java/NamingManager/setInitialContextFactoryBuilder/
date: 2021-01-11
key: Java.N.NamingManager
category: Java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamingManager.metodos valor="setInitialContextFactoryBuilder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setInitialContextFactoryBuilder(InitialContextFactoryBuilder builder) throws NamingException
~~~

## Parámetros
* **InitialContextFactoryBuilder builder**,  {% include w3api/param_description.html metodo=_dato parametro="InitialContextFactoryBuilder builder" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalStateException](/Java/IllegalStateException/), [NamingException](/Java/NamingException/)

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
