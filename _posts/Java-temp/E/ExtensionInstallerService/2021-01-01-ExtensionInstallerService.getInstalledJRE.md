---
title: ExtensionInstallerService.getInstalledJRE()
permalink: /Java/ExtensionInstallerService/getInstalledJRE/
date: 2021-01-11
key: Java.E.ExtensionInstallerService
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExtensionInstallerService.metodos valor="getInstalledJRE" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getInstalledJRE(URL url, String version)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}

## Clase Padre
[ExtensionInstallerService](/Java/ExtensionInstallerService/)

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
