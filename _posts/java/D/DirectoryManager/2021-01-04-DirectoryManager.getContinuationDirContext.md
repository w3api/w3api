---
title: DirectoryManager.getContinuationDirContext()
permalink: Java/DirectoryManager/getContinuationDirContext
date: 2021-01-04
key: JavaJava.D.DirectoryManager
category: java
tags: ['java se', 'javax.naming.spi', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectoryManager.metodos valor="getContinuationDirContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DirContext getContinuationDirContext(CannotProceedException cpe) throws NamingException
~~~

## Parámetros
* **CannotProceedException cpe**,  {% include w3api/param_description.html metodo=_data parametro="CannotProceedException cpe" %}

## Excepciones
[NamingException](/Java/NamingException/), [NamingManager.getContinuationContext(CannotProceedException)](/Java/NamingManager.getContinuationContext(CannotProceedException)/)

## Clase Padre
[DirectoryManager](/Java/DirectoryManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DirectoryManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
