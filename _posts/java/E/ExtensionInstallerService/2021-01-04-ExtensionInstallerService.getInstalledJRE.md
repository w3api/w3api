---
title: ExtensionInstallerService.getInstalledJRE()
permalink: Java/ExtensionInstallerService/getInstalledJRE
date: 2021-01-04
key: JavaJava.E.ExtensionInstallerService
category: java
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
* **String version**,  {% include w3api/param_description.html metodo=_data parametro="String version" %}
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}

## Clase Padre
[ExtensionInstallerService](/Java/ExtensionInstallerService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExtensionInstallerService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
