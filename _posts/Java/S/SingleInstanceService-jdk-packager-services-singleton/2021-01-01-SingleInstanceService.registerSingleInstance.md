---
title: SingleInstanceService.registerSingleInstance()
permalink: /Java/SingleInstanceService-jdk-packager-services-singleton/registerSingleInstance/
date: 2021-01-11
key: Java.S.SingleInstanceService-jdk-packager-services-singleton
category: Java
tags: ['java se', 'jdk.packager.services.singleton', 'jdk.packager.services', 'metodo java', 'Java 10']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SingleInstanceService-jdk-packager-services-singleton.metodos valor="registerSingleInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void registerSingleInstance(SingleInstanceListener slistener)
public static void registerSingleInstance(SingleInstanceListener slistener, boolean setFileHandler)
~~~

## Parámetros
* **SingleInstanceListener slistener**,  {% include w3api/param_description.html metodo=_dato parametro="SingleInstanceListener slistener" %}
* **boolean setFileHandler**,  {% include w3api/param_description.html metodo=_dato parametro="boolean setFileHandler" %}

## Clase Padre
[SingleInstanceService](/Java/SingleInstanceService-jdk-packager-services-singleton/)

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
