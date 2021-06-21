---
title: Configuration.findModule()
permalink: /Java/Configuration-java-lang-module/findModule/
date: 2021-01-11
key: Java.C.Configuration-java-lang-module
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Configuration-java-lang-module.metodos valor="findModule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Optional<ResolvedModule> findModule(String name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Clase Padre
[Configuration](/Java/Configuration-java-lang-module/)

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
