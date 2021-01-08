---
title: LinkerServices.getGuardedInvocation()
permalink: Java/LinkerServices/getGuardedInvocation
date: 2021-01-04
key: JavaJava.L.LinkerServices
category: java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkerServices.metodos valor="getGuardedInvocation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
GuardedInvocation getGuardedInvocation(LinkRequest linkRequest) throws Exception
~~~

## Parámetros
* **LinkRequest linkRequest**,  {% include w3api/param_description.html metodo=_data parametro="LinkRequest linkRequest" %}

## Excepciones
[Exception](/Java/Exception/)

## Clase Padre
[LinkerServices](/Java/LinkerServices/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkerServices.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
