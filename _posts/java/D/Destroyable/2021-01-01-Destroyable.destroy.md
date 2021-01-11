---
title: Destroyable.destroy()
permalink: Java/Destroyable/destroy
date: 2021-01-11
key: JavaJava.D.Destroyable
category: java
tags: ['java se', 'javax.security.auth', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.Destroyable.metodos valor="destroy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void destroy() throws DestroyFailedException
~~~

## Excepciones
[DestroyFailedException](/Java/DestroyFailedException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[Destroyable](/Java/Destroyable/)

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
