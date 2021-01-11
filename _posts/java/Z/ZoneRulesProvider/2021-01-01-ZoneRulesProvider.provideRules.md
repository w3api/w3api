---
title: ZoneRulesProvider.provideRules()
permalink: Java/ZoneRulesProvider/provideRules
date: 2021-01-11
key: JavaJava.Z.ZoneRulesProvider
category: java
tags: ['java se', 'java.time.zone', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZoneRulesProvider.metodos valor="provideRules" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract ZoneRules provideRules(String zoneId, boolean forCaching)
~~~

## Parámetros
* **String zoneId**,  {% include w3api/param_description.html metodo=_dato parametro="String zoneId" %}
* **boolean forCaching**,  {% include w3api/param_description.html metodo=_dato parametro="boolean forCaching" %}

## Excepciones
[ZoneRulesException](/Java/ZoneRulesException/)

## Clase Padre
[ZoneRulesProvider](/Java/ZoneRulesProvider/)

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
